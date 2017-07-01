#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QtGui>
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    socket = NULL;
    actimer=NULL;
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_link_clicked()
{
    socket = new QTcpSocket(this);
    connect(socket,SIGNAL(connected()),this,SLOT(net_connect()));
    connect(socket,SIGNAL(readyRead()),this,SLOT(net_recv()));
    connect(socket,SIGNAL(disconnected()),this,SLOT(dis_connect()));
    socket->connectToHost(ui->ip->text(),8888);
 //   socket->write("6",2);
    if(actimer==NULL)
    {
        actimer =new QTimer(this);
    }
    connect(actimer,SIGNAL(timeout()),this,SLOT(send_request()));
    actimer->start(2000);

}
void MainWindow::on_lon_clicked()
{
   // socket->connectToHost(ui->ip->text(),8888);
    socket->write("0",2);
}
void MainWindow::on_loff_clicked()
{
 //   socket->connectToHost(ui->ip->text(),8888);
    socket->write("1",2);
}
void MainWindow::send_request()
{
//    socket->connectToHost(ui->ip->text(),8888);
    socket->write("get",4);
}

void MainWindow::on_quit_clicked()
{
  //socket->write("7",2);
    QApplication::exit();
}
void MainWindow::dis_connect()
{
    socket->close();
}

void MainWindow::net_recv()
{
    char recv[36],str[36];
    int id;
    float tmp,hum;
    socket->read(recv,sizeof(recv));
#if 1
    sscanf(recv,"%did%ftmp%fhum",&id,&tmp,&hum);
    snprintf(str,sizeof(str),"id  is %d",id);
    ui->id->setText(str);
    snprintf(str,sizeof(str),"tmp is %.2f",tmp);
    ui->tmp->setText(str);
    snprintf(str,sizeof(str),"hum is %.2f",hum);
    ui->hum->setText(str);
#else
    ui->tmp->setText(recv);
    ui->hum->setText(recv);

#endif

}

void MainWindow::on_fon_clicked()
{
  //  socket->connectToHost(ui->ip->text(),8888);
    socket->write("4",2);
}

void MainWindow::on_foff_clicked()
{
  //  socket->connectToHost(ui->ip->text(),8888);
    socket->write("5",2);
}

void MainWindow::on_bon_clicked()
{
   // socket->connectToHost(ui->ip->text(),8888);
    socket->write("2",2);
}

void MainWindow::on_boff_clicked()
{
   // socket->connectToHost(ui->ip->text(),8888);
    socket->write("3",2);
}
