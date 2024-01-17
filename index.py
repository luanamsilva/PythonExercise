def addContact(contacts, name, phone, email):
  contact = {"name": name, "phone": phone, "email": email, "favorite": False}
  contacts.append(contact)
  print(f"Contato adicionado!")
  return

def contactsList(contacts):
  print("\nContatos adicionados: ")
  for index, contact in enumerate(contacts, start=1):
    status = "Sim" if contact["favorite"] else "Não"
    print(f"{index}- Nome: {contact['name']}/ Telefone: {contact['phone']}/ e-mail: {contact['email']}/ Favorito: [{status}]")
  return

def updateContact(contacts, index, newNameContact, newPhone, newEmail):
  indexContactUpdate = int(index)-1
  if indexContactUpdate >=0 and indexContactUpdate < len(contacts):
    contacts[indexContactUpdate]["name"] = newNameContact
    contacts[indexContactUpdate]["phone"] = newPhone
    contacts[indexContactUpdate]["email"] = newEmail
    print(f"Contato {index}, atualizado para {newNameContact} - {newPhone} - {newEmail}")
  return

def favoriteContact(contacts, index):
  indexContactUpdate = int(index)-1
  if indexContactUpdate >=0 and indexContactUpdate < len(contacts):
   contacts[indexContactUpdate]["favorite"] = not contacts[indexContactUpdate]["favorite"]
   print(f"Status favorito do contato {index} modificado com sucesso!")
  return

def deleteContact(contacts, index):
  indexContactUpdate = int(index)-1
  if indexContactUpdate >=0 and indexContactUpdate < len(contacts):
    removedContact = contacts.pop(indexContactUpdate)
    print(f"Tarefa removida: {removedContact}")
  return

contacts = []

while True:
  print("\n Menu da sua agenda - Escolha a opção desejada: ")
  print("1- Adicionar um novo contato ")
  print("2- Ver os contatos de sua agenda ")
  print("3- Editar contato ")
  print("4- Tornar um contato favorito ")
  print("5 - Deletar um contato ")
  print("6- Sair")
  
  choice = input("Digite a opção desejada: ")
  
  if(choice == "1"):
    contactName = input("Digite o nome do contato a ser adicionado: ")
    contactPhone = input("Digite o telefone: ")
    contactEmail = input("Digite o email do contato: ")
    addContact(contacts, contactName, contactPhone, contactEmail)
    
  elif(choice == "2"):
    contactsList(contacts)
  
  elif(choice == "3"):
    contactsList(contacts)
    indexContact = input("Digite o índice do contato que deseja atualizar: ")
    newNameContact= input("Digite o nome atualizado: ")
    newPhone= input("Digite o telefone atualizado: ")
    newEmail= input("Digite o e-mail atualizado: ")
    updateContact(contacts, indexContact, newNameContact, newPhone, newEmail )
    
  elif(choice == "4"):
    indexContact = input("Digite o índice do contato que deseja alterar o status favorito: ")
    favoriteContact(contacts, indexContact)
    
  elif choice == "5":
    contactsList(contacts)
    indexContact = input("Digite o índice do contato que deseja deletar: ")
    deleteContact(contacts, indexContact)

  elif choice == "6":
    print("Programa finalizado!")
    break
  