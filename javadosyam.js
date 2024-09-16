const fs = require('fs');
const readline = require('readline');

const filePath = 'notes.txt';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function showMenu() {
    console.log('\nSimple Note-taking App');
    console.log('1. Add Note');
    console.log('2. List Notes');
    console.log('3. Delete Note');
    console.log('4. Exit');
    rl.question('Choose an option: ', (option) => {
        switch (option) {
            case '1':
                addNote();
                break;
            case '2':
                listNotes();
                break;
            case '3':
                deleteNote();
                break;
            case '4':
                rl.close();
                break;
            default:
                console.log('Invalid choice.');
                showMenu();
                break;
        }
    });
}

function addNote() {
    rl.question('Enter note content: ', (content) => {
        fs.appendFile(filePath, content + '\n', (err) => {
            if (err) throw err;
            console.log('Note added.');
            showMenu();
        });
    });
}

function listNotes() {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) throw err;
        console.log('\nNotes:');
        console.log(data || 'No notes available.');
        showMenu();
    });
}

function deleteNote() {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) throw err;
        const notes = data.trim().split('\n');
        if (notes.length === 0) {
            console.log('No notes to delete.');
            showMenu();
            return;
        }

        console.log('\nNotes:');
        notes.forEach((note, index) => console.log(`${index + 1}. ${note}`));

        rl.question('Enter the number of the note to delete: ', (number) => {
            const noteIndex = parseInt(number, 10) - 1;
            if (noteIndex >= 0 && noteIndex < notes.length) {
                notes.splice(noteIndex, 1);
                fs.writeFile(filePath, notes.join('\n'), (err) => {
                    if (err) throw err;
                    console.log('Note deleted.');
                    showMenu();
                });
            } else {
                console.log('Invalid number.');
                showMenu();
            }
        });
    });
}

showMenu();
