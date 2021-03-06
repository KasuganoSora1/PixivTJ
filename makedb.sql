CREATE DATABASE IF NOT EXISTS pixivtj;
USE pixivtj;
CREATE TABLE IF NOT EXISTS User(
    userId VARCHAR(10) NOT NULL PRIMARY KEY,
    name VARCHAR(100),
    image VARCHAR(500),
    imageBig VARCHAR(500),
    premium BOOLEAN,
    isFollowed BOOLEAN,
    isMypixiv BOOLEAN,
    isBlocking BOOLEAN,
    background VARCHAR(500),
    sketchLiveId VARCHAR(50),
    partial INT,
    acceptRequest BOOLEAN
);
CREATE TABLE IF NOT EXISTS Illust(
    illustid VARCHAR(10) NOT NULL PRIMARY KEY,
    illustTitle VARCHAR(500),
    illustComment VARCHAR(5000),
    id VARCHAR(10),
    title VARCHAR(500),
    description VARCHAR(5000),
    illustType INT,
    createDate DATETIME,
    uploadDate DATETIME,
    pixiv_restrict INT,
    xRestrict INT,
    sl INT,
    url_mini VARCHAR(500),
    url_thumb VARCHAR(500),
    url_small VARCHAR(500),
    url_regular VARCHAR(500),
    url_original VARCHAR(500),
    alt VARCHAR(500),
    userId VARCHAR(10),
    userName VARCHAR(100),
    userAccount VARCHAR(100),
    likeData BOOLEAN,
    width INT,
    height INT,
    pageCount INT,
    bookmarkCount INT,
    likeCount INT,
    commentCount INT,
    responseCount INT,
    viewCount INT,
    bookStyle INT,
    isHowto BOOLEAN,
    isOriginal BOOLEAN,
    imageResponseCount INT,
    pollData VARCHAR(50),
    seriesNavData VARCHAR(50),
    descriptionBoothId VARCHAR(50),
    descriptionYoutubeId VARCHAR(50),
    comicPromotion VARCHAR(50),
    fanboxPromotion VARCHAR(50),
    isBookmarkable BOOLEAN,
    contestData VARCHAR(50),
    isUnlisted BOOLEAN,
    request VARCHAR(50),
    commentOff VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Tag(
    tag VARCHAR(100) NOT NULL PRIMARY KEY,
    locked BOOLEAN,
    deletable BOOLEAN,
    userId VARCHAR(10),
    translation_name VARCHAR(100),
    userName VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS IllustTag(
    tag VARCHAR(100),
    illustid VARCHAR(100),
    PRIMARY KEY(tag,illustid)
);

CREATE TABLE IF NOT EXISTS ErrorIllust(
    illustId VARCHAR(10) NOT NULL PRIMARY KEY,
    reason VARCHAR(50),
    detail VARCHAR(5000)
)

ALTER TABLE Illust ADD INDEX(createDate);
ALTER TABLE IllustTag Add INDEX(tag);
ALTER TABLE IllustTag Add INDEX(illustid);
ALTER TABLE ErrorIllust ADD INDEX(reason);