/**
 * ============================================
 * ADAPTIVE LEARNING AGENT - FRONTEND API
 * Shared JavaScript for API integration
 * ============================================
 */


// Backend Base URL - Production Render URL
const API_BASE = "https://learning-agent-backend.onrender.com";


/**
 * Make API request to backend
 * @param {string} endpoint - API endpoint (e.g., '/student', '/plan/123')
 * @param {object} options - Fetch options (method, body, etc.)
 * @returns {Promise<object>} - Parsed JSON response
 */
async function apiRequest(endpoint, options = {}) {
    const url = `${API_BASE}${endpoint}`;
    
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const config = {
        ...defaultOptions,
        ...options,
        headers: {
            ...defaultOptions.headers,
            ...(options.headers || {}),
        },
    };

    try {
        console.log(`Making API request to: ${url}`);
        const response = await fetch(url, config);

        if (!response.ok) {
            const errorText = await response.text();
            let errorData = {};
            try {
                errorData = JSON.parse(errorText);
            } catch {
                errorData = { message: errorText };
            }
            console.error('API Error:', errorData);
            throw new Error(
                errorData.message || 
                errorData.detail || 
                errorData.error ||
                `HTTP error! status: ${response.status}`
            );
        }

        const data = await response.json();
        console.log('API Response:', data);
        return data;
    } catch (error) {
        // Handle network errors
        console.error('API Request Error:', error);
        if (error.name === 'TypeError' && error.message.includes('fetch')) {
            throw new Error(`Network error: Could not connect to backend at ${url}. The Render backend may be sleeping (free tier). Try refreshing the page or check if the backend is running.`);
        }
        throw error;
    }
}

/**
 * Get student ID from localStorage
 * @returns {string|null} - Student ID or null
 */
function getStudentId() {
    return localStorage.getItem('student_id');
}

/**
 * Check if student is logged in
 * @returns {boolean}
 */
function isStudentLoggedIn() {
    return !!getStudentId();
}

/**
 * Redirect to onboarding if student not logged in
 */
function requireStudent() {
    if (!isStudentLoggedIn()) {
        window.location.href = 'index.html';
    }
}

/**
 * Format date/time for display
 * @param {string|Date} date - Date to format
 * @returns {string} - Formatted date string
 */
function formatDate(date) {
    if (!date) return '';
    
    const d = new Date(date);
    if (isNaN(d.getTime())) return date;
    
    return d.toLocaleString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

/**
 * Show error message in a container
 * @param {HTMLElement} container - Container element
 * @param {string} message - Error message
 */
function showError(container, message) {
    container.innerHTML = `<div class="error-message">${message}</div>`;
    container.style.display = 'block';
}

/**
 * Show success message in a container
 * @param {HTMLElement} container - Container element
 * @param {string} message - Success message
 */
function showSuccess(container, message) {
    container.innerHTML = `<div class="success-message">${message}</div>`;
    container.style.display = 'block';
}

/**
 * Validate student form data
 * @param {object} data - Student data
 * @returns {object} - {valid: boolean, errors: string[]}
 */
function validateStudentData(data) {
    const errors = [];

    if (!data.name || data.name.trim().length === 0) {
        errors.push('Name is required');
    }

    if (!data.class_level || data.class_level.trim().length === 0) {
        errors.push('Class level is required');
    }

    if (!data.subject) {
        errors.push('Subject is required');
    }

    if (!data.goal) {
        errors.push('Goal is required');
    }

    if (!data.language) {
        errors.push('Language is required');
    }

    if (!data.daily_time || data.daily_time < 15 || data.daily_time > 480) {
        errors.push('Daily study time must be between 15 and 480 minutes');
    }

    return {
        valid: errors.length === 0,
        errors
    };
}

// Export functions for use in other scripts (if using modules)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        apiRequest,
        getStudentId,
        isStudentLoggedIn,
        requireStudent,
        formatDate,
        showError,
        showSuccess,
        validateStudentData,
        API_BASE
    };
}
