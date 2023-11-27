using MyMessenger;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using Message = MyMessenger.Message;

namespace WindowsFormsClient
{
    public partial class Form1 : Form
    {
        private static int MessageID = 0;
        private static string UserName;
        private static MessangerClientAPI API = new MessangerClientAPI();
        public Form1()
        {
            InitializeComponent();
            MessageTB.Enabled = false;
        }

        private void SendButton_Click(object sender, EventArgs e)
        {
            
        }

        private void label3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
        private void label3_MouseLeave(object sender, EventArgs e)
        {
            label3.BackColor = Color.FromArgb(255, 158, 19, 32);
        }

        private void label3_MouseEnter(object sender, EventArgs e)
        {
            label3.BackColor = Color.FromArgb(255, 189, 23, 45);
        }

        private void label4_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }

        private void label4_MouseEnter(object sender, EventArgs e)
        {
            label4.BackColor = Color.FromArgb(255, 14, 237, 233);
        }

        private void label4_MouseLeave(object sender, EventArgs e)
        {
            label4.BackColor = Color.FromArgb(255, 85, 220, 250);
        }

        private void ConnectDisconnectBT_Click(object sender, EventArgs e)
        {
            if (ConnectDisconnectBT.Text == "Подключиться")
            {
                UserNameTB.Enabled = false;
                MessageTB.Enabled = true;
                ConnectDisconnectBT.Text = "Отключиться";
            }
            else
            {
                UserNameTB.Enabled = true;
                MessageTB.Enabled = false;
                ConnectDisconnectBT.Text = "Подключиться";
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            var getMessage = new Func<Task>(async () =>
            {
                MyMessenger.Message msg = await API.GetMessageHTTPAsync(MessageID);
                while (msg != null)
                {
                    MessagesLB.Items.Add(msg);
                    MessageID++;
                    msg = await API.GetMessageHTTPAsync(MessageID);
                }
            });
            getMessage.Invoke();
        }

        private void MessageTB_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                string UserName = UserNameTB.Text;
                string Message = MessageTB.Text;
                if ((UserName.Length > 1) && (UserName.Length > 1))
                {
                    MyMessenger.Message msg = new MyMessenger.Message(UserName, Message, DateTime.Now);
                    API.SendMessage(msg);
                }
                MessageTB.Text = null;
            }
            
        }
    }
}
