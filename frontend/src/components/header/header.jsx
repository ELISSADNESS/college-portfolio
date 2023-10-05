import React from "react";

import Button from "../button/button";

import styles from "./header.module.css";

function Header() {
    return (
        <>
            <h1 className={styles.title}>Работы<br />студентов</h1>
            <Button>Все работы</Button>
            <Button>Иллюстрации</Button>
            <Button>Фото</Button>
            <Button>Шрифты</Button>
        </>
    );
}

export default Header;