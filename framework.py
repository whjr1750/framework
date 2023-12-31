from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from web3 import Web3

root = Tk()
root.title("CryptoTrade")

root.configure( background='white')

infura_url = 'https://sepolia.infura.io/v3/544d61c946ac4800be3ff4ad3db011e1'

web3_infura_connection = Web3(Web3.HTTPProvider(infura_url))

image_logo = ImageTk.PhotoImage(Image.open("logo.jpeg"))
image_label = Label(root, image=image_logo)
image_label.pack(side="top")

frame = Frame(
	root, 
	bg='white',
	padx=5,
	pady=5
)

Label(frame, text="Account Number 1: ",fg='black',bg='white').grid(row=0,column=0, sticky=W, pady=10)

Label(frame, text="Account Number 2: ",fg='black',bg='white').grid(row=1,column=0, sticky=W, pady=10)

Label(frame, text="Private Key: ",fg='black',bg='white').grid(row=2,column=0, sticky=W, pady=10)

Label(frame, text="ETH: ",fg='black',bg='white').grid(row=3,column=0, sticky=W, pady=10)

Label(frame, text="Gas Price (GWEI): ",fg='black',bg='white').grid(row=4,column=0, sticky=W, pady=10)

Label(frame, text="Gas Limit (GWEI): ",fg='black',bg='white').grid(row=5,column=0, sticky=W, pady=10)


account1 = Entry(frame)

account2 = Entry(frame)

private_key = Entry(frame)

amount = Entry(frame)

gas_price = Entry(frame)

gas_limit = Entry(frame)

account1.grid(row=0, column=1, pady=10, padx=20)
account2.grid(row=1, column=1, pady=10, padx=20)
private_key.grid(row=2, column=1, pady=10, padx=20)
amount.grid(row=3, column=1, pady=10, padx=20)
gas_price.grid(row=4, column=1, pady=10, padx=20)
gas_limit.grid(row=5, column=1, pady=10, padx=20)

def sendETH():
	account1_id = account1.get()
	account2_id = account2.get()
	key = private_key.get()
	eth_amount = amount.get()
	gas_fee = gas_price.get()
	Glimit = gas_limit.get()

	nonce = web3_infura_connection.eth.getTransactionCount(account1_id)
	transaction = {
	'nonce': nonce,
	'to': account2_id,
	'value': web3_infura_connection.toWei(eth_amount, 'amount'),
	'gas': int(Glimit),
	'gasPrice': web3_infura_connection.toWei(gas_fee, 'gwei'),
	}

	signed_transaction = web3_infura_connection.eth.account.signTransaction(transaction, key)
	transaction_hash = web3_infura_connection.eth.sendRawTransaction(signed_transaction.rawTransaction)#rawTransaction is inBuilt function.due to which it was throwing error.

	print('Your transaction is successfully done! Your transaction ID is ', transaction_hash.hex())
	messagebox.showinfo('Transaction status:-', '"Succcessful" verify through you metamask wallet.')


frame.pack()

transfer_eth = Button(root, text='Transfer ETHER', command=sendETH, highlightbackground='white', width=15)
transfer_eth.pack()

root.mainloop()