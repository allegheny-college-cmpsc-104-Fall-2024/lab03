def group_religions(religion):
    christian_denominations = [
        "7th Day Adventists", "African Methodist Ep", "Assembly of God", "Baptist",
        "Byzantine Catholic", "Episcopalian", "Christ. & Miss. All.", "Christian Disciples",
        "Christian Scientist", "Church of God", "Evangelical", "Greek Orthodox",
        "JC Latter-Day Saints", "Jehovah's Witness", "Lutheran", "Mennonite",
        "Nazarene", "Orthodox", "Other Christian", "Pentecostal", "Presbyterian",
        "Quaker", "Roman Catholic", "Russian Orthodox", "United Methodist",
        "Utd. Chrch of Christ", "Wesleyan"
    ]
    non_christian_religions = [
        "Sikh", "Hindu", "Jewish", "Buddhist", "Muslim", "Other Non Christian",
        "Pagan/Wiccan", "Unitarian/Universal"
    ]
    no_religion = ["Agnostic", "Atheist", "Unaffiliated", "None"]

    if religion in christian_denominations:
        return "christian"
    elif religion in non_christian_religions # Syntax error: missing colon
        return "non-christian"
    elif religion in no_religion:
        return "no religion"
    else:
        return religion

# Example
religion = group_religions("Baptist")
if religion:
    print(religion)