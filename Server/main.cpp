#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include <windows.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <iphlpapi.h>
#include <stdio.h>

#pragma comment(lib, "Ws2_32.lib")

#define DEFAULT_PORT "27015"

int main() {
  printf("Program Started\n");
  WSADATA wsaData;
  int iResult;

  //initialize winsock
  iResult = WSAStartup(MAKEWORD(2,2), &wsaData);
  if (iResult != 0) {
    printf("WSAStartup failed: %d\n", iResult);
    return 1;
  }
  printf("WSAStartup was successful\n", iResult);
  struct addrinfo *result = NULL, *ptr = NULL, hints;
  ZeroMemory(&hints, sizeof (hints));
  hints.ai_family = AF_INET;
  hints.ai_socktype = SOCK_STREAM;
  hints.ai_protocol = IPPROTO_TCP;
  hints.ai_flags = AI_PASSIVE;

  //resolve the local address and port to be used by the server
  iResult = getaddrinfo(NULL, DEFAULT_PORT, &hints, &result);
  if (iResult != 0) {
    printf("Getaddrinfo failed %d\n", iResult);
    WSACleanup();
    return 1;
  }
  printf("Getaddrinfo succeded");
  SOCKET ListenSocket = INVALID_SOCKET;
  ListenSocket = socket(result->ai_family, result->ai_socktype, result->ai_protocol);
  if (ListenSocket == INVALID_SOCKET) {
    printf("Error at socket(): %d\n", WSAGetLastError());
    freeaddrinfo(result);
    WSACleanup();
    return 1;
  }
  printf("Sucessfully created socket()\n");

  //Setup the TCP listening socket
  iResult = bind(ListenSocket, result->ai_addr, (int)result->ai_addrlen);
  if (iResult == SOCKET_ERROR) {
    printf("Bind failed with error %d\n", WSAGetLastError());
    freeaddrinfo(result);
    closesocket(ListenSocket);
    WSACleanup();
    return 1;
  }
  freeaddrinfo(result);
  printf("Sucessfully created socket.");
  if (listen(ListenSocket, SOMAXCONN) == SOCKET_ERROR) {
    printf("Listen failed with error %ld\n", WSAGetLastError());
    closesocket(ListenSocket);
    WSACleanup();
    return 1;
  }
  printf("Listen succeded");
  SOCKET ClientSocket;
  ClientSocket = INVALID_SOCKET;
  ClientSocket = accept(ListenSocket, NULL, NULL);
  if (ClientSocket == INVALID_SOCKET) {
    printf("accept failed: %d\n", WSAGetLastError());
    closesocket(ListenSocket);
    WSACleanup();
    return 1;
  }
  printf("Sucessfully connected to client socket.");


  #define DEFAULT_BUFLEN 512

  char recvbuf[DEFAULT_BUFLEN];
  int Iresult, iSendResult;
  int recvbuflen = DEFAULT_BUFLEN;

  //recieve until the peer shuts down the connection
  do {

    iResult = recv(ClientSocket, recvbuf, recvbuflen, 0);
    if (iResult > 0) {
        printf("Bytes recieved: %d\n", iResult);

        iSendResult = send(ClientSocket, recvbuf, iResult, 0);
        if (iSendResult == SOCKET_ERROR) {
            printf("Send failed: %d\n", iSendResult);
            closesocket(ClientSocket);
            WSACleanup();
            return 1;
        }
        printf("Bytes Sent: %d\n", iSendResult);

    } else if (iResult == 0) {
        printf("Connection closing.../n");
    }
    else {
        printf("recv failed: %d\n", WSAGetLastError());
        closesocket(ClientSocket);
        WSACleanup();
        return 1;
    }

  } while (Iresult > 0);
