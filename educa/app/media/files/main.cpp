#include "socket.h"
#include <QApplication>
#include<stdio.h>
#include<winsock2.h>
#include <ws2tcpip.h>
#include <windows.h>
#include <iphlpapi.h>
#pragma comment(lib,"ws2_32.lib") //Winsock Library

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Socket w;
    w.show();
    WSADATA wsa;

      printf("\nInitialising Winsock...");
      if (WSAStartup(MAKEWORD(2,2),&wsa) != 0)
      {
          printf("Failed. Error Code : %d",WSAGetLastError());
          return 1;
      }

      printf("Initialised.");

    return a.exec();
}
