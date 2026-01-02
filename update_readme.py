from datetime import datetime

def update_readme():
    """
    Atualiza o README.md a partir do template, substituindo o placeholder
    pelos dias restantes no ano atual.
    """

    next_year = datetime.now().year + 1
    current_year = datetime.now().year
    days_left = (datetime(next_year, 1, 1) - datetime.now()).days
    
    # Lê o template
    with open('README_template.md', 'r', encoding='utf-8') as file:
        template_content = file.read()
    
    # Substitui o placeholder pelos dias restantes
    updated_content = template_content.replace("{{DAYS_REMAINING}}", str(days_left)).replace("{{CURRENT_YEAR}}", str(current_year))
    
    # Escreve o README final
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"README.md atualizado! Restam {days_left} dias em {current_year}.")



if __name__ == "__main__":
    update_readme()
    