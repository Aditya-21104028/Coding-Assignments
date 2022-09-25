#include <iostream>
using namespace std;

// creating a doubly linked list:
class node{                                   
    public:
    string data;
    node* next;
    node* prev;

    node(string name, string val){
        data = name+" "+val;
        next = NULL;
        prev = NULL;
    }
};

//inserting a note at head:
void insertAtHead(node* &head, string name, string val){              
    node* n = new node(name, val);

    n->next = head;
    if(head != NULL){                        
        head->prev = n;
    }
    head = n;
}

//inserting a node at tail:
void insertAtTail(node* &head, string name, string val){
    node* n = new node(name, val);
    
    if(head == NULL){
        insertAtHead(head, name, val);
        return;
    }

    node* temp = head;
    while(temp->next != NULL){
        temp = temp->next;
    }
    temp->next = n;
    n->prev = temp;
}

//printing the doubly linked list:
void display(node* head){
    node* temp = head;

    while(temp != NULL){
        cout<<temp->data<<"<->";
        temp = temp->next;
    }
    cout<<"NULL"<<endl;
}

int main(){
    node* head = NULL;
    int family;
    cout<<"Enter the total number of family members: ";
    cin>>family;
    for(int i=1; i<=family; i++){
        string name, val;
        cout<<"Enter name and age of family member "<<i<<": ";
        cin>>name>>val;
        insertAtTail(head, name, val);
    }
    cout<<endl;
    cout<<"Your doubly-linked list is as follows:"<<endl;
    display(head);
    
    return 0;
}