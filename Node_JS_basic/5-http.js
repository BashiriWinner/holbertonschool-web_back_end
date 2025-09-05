const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.trim().split('\n').slice(1); // Skip header
    const students = lines.filter((line) => line.trim() !== '');
    const fields = {};

    students.forEach((line) => {
      const [firstName, , , field] = line.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    });

    const result = [`Num of students: ${students.length}`];
    for (const [field, names] of Object.entries(fields)) {
      result.push(`Num of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
    return result;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
