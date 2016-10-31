import psycopg
#TODO: figure out how the id sequencing works to ensure I'm getting all the most recent stories
source_list = [230]


def create_query(source_list, last_story):
    """Takes a list of source IDs and the story id of thelast story created
    and returns a list of stories published since then"""
    source_string = ''
    source_string = source_string + str(source_list[0])

    for i in range(1:len(source_list)):
        source_string = source_string + ', ' + str(source_list[i])

    story_query = """
    select
    	n.id
    	, n.news_source_id
    	, src.name
    	, n.original_text
    	, n.created_date
    	--, nber.business_entity_id
    from news n
    	inner join news_source src on n.news_source_id = src.entity_id
    	--inner join news_be_relation nber on nber.news_id = n.id
    where
    	src.entity_id in (""" + source_string + """)
        and n.id > """ + last_story + """
    order by CAST(n.created_date as DATE) desc, n.id desc
    """
    return story_query


def call_pg(story_query):
    #Call postgres and return a list of stories
    stories = []
    for result in results:
        story = {}
        story['text'] = "Some text here" #swap with db return
        story['created_date'] =


if __name__ == '__main__':
    source_list = [230]
    last_story = 53866613178338370
    create_query(source_list, last_story)
