CREATE TABLE `products` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `title` VARCHAR(255) NOT NULL UNIQUE,
  `price` FLOAT DEFAULT 0,
  `description` TEXT,
  `category` VARCHAR(100),
  `image` VARCHAR(512),
  `rating_rate` FLOAT DEFAULT 0,
  `rating_count` INT DEFAULT 0,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  
  INDEX `idx_title` (`title`),
  INDEX `idx_price` (`price`),
  INDEX `idx_category` (`category`),
  INDEX `idx_rating_rate` (`rating_rate`),
  INDEX `idx_created_at` (`created_at`),
  INDEX `idx_updated_at` (`updated_at`)
);
